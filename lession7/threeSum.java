public class Solution
{
	public List<List<Integer>> threeSum(int[] nums)
	{
		List<List<Integer>> list = new LinkedList<List<Integer>>();
		Arrays.sort(nums);

		for (int i = 0; i < nums.length - 2; i++)
		{
			if (i > 0 && nums[i] == nums[i - 1])
			{
				continue;
			}

			int lo = i + 1;
			int hi = nums.length - 1;

			int target = 0 - nums[i];

			while(lo < hi)
			{
				if (nums[lo] + nums[hi] == target)
				{
					List<Integer> cur = new LinkedList<Integer>();
					cur.add(nums[i]);
					cur.add(nums[lo]);
					cur.add(nums[hi]);
					list.add(cur);

					while(lo < hi && nums[lo] == nums[lo + 1])
					{
						lo++;
					}

					while(lo < hi && nums[hi] == nums[hi - 1])
					{
						hi--;
					}

					hi--;
					lo++;
				}
				else if (nums[lo] + nums[hi] < target)
				{
					lo++;
				}
				else
				{
					hi--;
				}
			}
		}

		return list;
	}
}