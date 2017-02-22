public class Solution
{
	public int threeSumClosest(int[] nums, int target)
	{
		if (nums.length < 3)
		{
			return 0;
		}

		Arrays.sort(nums);

		int result = nums[0] + nums[1] + nums[nums.length - 1];

		for (int i = 0; i < nums.length - 2; i++)
		{
			int lo = i + 1;
			int hi = nums.length - 1;

			while(lo < hi)
			{
				if (Math.abs(target - nums[i] - nums[lo] - nums[hi]) < Math.abs(target - result))
				{
					result = nums[i] + nums[lo] + nums[i];
				}
				else if (target > nums[i] + nums[lo] + nums[hi])
				{
					lo++;
				}
				else
				{
					hi--;
				}
			}
		}

		return result;
	}
}