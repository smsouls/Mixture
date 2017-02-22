public class Solution
{
	public List<String> letterCombinations(String digits)
	{
		List<String> list = new ArrayList<String>();
		if (digits.length() < 1)
		{
			return list;
		}

		String[] digitalLetter = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

		list.add("");

		for (int i = 0; i <digits.length(); i++)
		{
			list = combine(digitalLetter[digits.charAt(i) - '0'], list);
		}

		return list;
	}

	private List<String> combine(String digit, List<String> l)
	{
		List<String> list = new ArrayList<String>();
		for (int i = 0; i < digit.length(); i++)
		{
			for (String s : l)
			{
				list.add(s + digit.charAt(i))
			}
		}

		return list;
	}


}