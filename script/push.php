<?php
// devicetoken
 $deviceToken = '4798f93509ce7ea129f4d69206f4eb8b846eada9fb4936678af6635b8463b9c4';
// 私钥密码，生成pem的时候输入的
$passphrase = '1234';
// 定制推送内容，有一点的格式要求，详情Apple文档
$message = array(
    'body'=>'你收到一个新订单'
);
$body['aps'] = array(
    'alert' => $message,
    'sound' => 'default',
    'badge' => 100,
    );
$body['type']=3;
$body['msg_type']=4;
$body['title']='新订单提醒';
$body['msg']='你收到一个新消息';

// $ctx = stream_context_create();
$ctx = stream_context_create([
            'ssl' => [
                'verify_peer'      => true,
                'verify_peer_name' => true,
                'cafile'           => 'entrust_2048_ca.cer',
            ]
        ]);
stream_context_set_option($ctx, 'ssl', 'local_cert', 'ck.pem');//记得把生成的push.pem放在和这个php文件同一个目录
stream_context_set_option($ctx, 'ssl', 'passphrase', $passphrase);
$fp = stream_socket_client(
    //这里需要特别注意，一个是开发推送的沙箱环境，一个是发布推送的正式环境，deviceToken是不通用的
    'ssl://gateway.sandbox.push.apple.com:2195', $err,
    //'ssl://gateway.push.apple.com:2195', $err,
    $errstr, 60, STREAM_CLIENT_CONNECT|STREAM_CLIENT_PERSISTENT, $ctx);
if (!$fp)
    exit("Failed to connect: $err $errstr" . PHP_EOL);
echo 'Connected to APNS' . PHP_EOL;
$payload = json_encode($body);
$msg = chr(0) . pack('n', 32) . pack('H*', $deviceToken) . pack('n', strlen($payload)) . $payload;
$result = fwrite($fp, $msg, strlen($msg));
if (!$result)
    echo 'Message not delivered' . PHP_EOL;
else
    echo 'Message successfully delivered' . PHP_EOL;
fclose($fp);
?>