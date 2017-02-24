public class Solution
{
	public int maxArea(int[] height)
	{
		int max = 0;
		int left = 0;
		int right = height.length - 1;

		while (left < right)
		{
			max = Math.max(max, area(height, left, right));
		}

		return max;	
	}

	public int area(int[] height, int k, int j)
	{
		return Math.min(height[k], height[j]) * (j - k);
	}
}