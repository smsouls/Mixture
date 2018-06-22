public class Solution
{
	public String convert(String s, int numRows)
	{
		if (numRows < 2)
		{
			return s;
		}

		StringBuffer[] sb = new StringBuffer[numRows];
		for (int i = 0; i < numsRows; i++)
		{
			sb[i] = new StringBuffer();
		}

		int index = 0;
		int increase = 1;

		for (int i = 0; i < s.length(); i++)
		{
			sb[index] = s.charAt(i);

			if (index == 0)
			{
				increase = 1;
			}

			if (index == numRows - 1)
			{
				increase = -1;
			}

			index += increase;
		}

		String res = "";
		for (int i = 0; i < numRows; i++)
		{
			res += sb[i];
		}

		return res.toString();
	}
}