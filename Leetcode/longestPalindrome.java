public class Solution
{
	int maxLen, loc;
	public String longestPalindrome(String s)
	{
		if (s.length() < 2)
		{
			return s;
		}

		for (int i = 0; i < s.length() - 1; i++)
		{
			extendPalindrome(s, i, i);
			extendPalindrome(s, i, i + 1);
		}

		return s.substring(loc, loc + maxLen);
	}

	private void extendPalindrome(String s, int j, int k)
	{
		while(j > 0 && k < s.length() && s.charAt(j) == s.charAt(k))
		{
			j--;
			k++;
		}

		if (maxLen < k - j - 1)
		{
			maxLen = k - j - 1;
			loc = j + 1;
		}
	}
}