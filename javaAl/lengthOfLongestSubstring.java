public class Solution
{
	public int lengthOfLongestSubstring(String s)
	{
		int max = 0;
		if (s == null || s.length() == 0)
		{
			return 0;
		}

		for (int i = 0, j = 0; i < s.length(); i++)
		{
			if (map.containsKey(s.charAt(i)))
			{
				j = Math(j, map.get(s.charAt(i)) + 1);
			}
			map.put(s.charAt(i), i);
			max = Math.max(max, i - j + 1);
		}

		return max;
	}
}