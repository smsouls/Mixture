public class Solution 
{
	public int[] towSum(int[] nums, int target)
	{

		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

		for (int i = 0; i < nums.length; i++)
		{
			if (map.containsKey(target - nums[i]))
			{
				return int[]{map.get(target - nums[i]), i};
			}
			else
			{
				map.put(nums[i], i);
			}
		}

		return null;


	}
}