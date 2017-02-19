public class Solution
{
	public double findMedianSortedArrays(int[] nums1, int[] nums2)
	{
		int len1 = nums1.length;
		int len2 = nums2.length;
		int sumLen = len1 + len2;

		if (sumLen == 0)
		{
			return 0;
		}

		if (sumLen%2 != 0)
		{
			return findKthSmallest(nums1, len1, 0, nums2, len2, 0, sumLen/2 + 1);
		}
		else
		{
			return (findKthSmallest(nums1, len1, 0, nums2, len2, 0, sumLen/2) + findKthSmallest(nums1, len1, 0, nums2, len2, 0, sumLen/2 + 1))/2.0; 
		}
	}


	private static int findKthSmallest(int[] a, int m, int begin1, int[] b, int n, int begin2, int k)
	{
		if (m > n)
		{
			findkThSmallest(b, n, begin2, a, m, begin1, k);
		}

		if (m == 0)
		{
			return b[begin2 + k - 1];
		}

		int partA = Math.min(m, k/2);
		int partB = k - partA;

		if (a[begin1 + partA - 1] == b[begin2 + partB - 1])
		{
			return a[begin1 + partA - 1];
		}
		else if (a[begin1 + partA - 1] > b[begin2 + partB - 1])
		{
			return findKthSmallest(a, m, begin, b, n - partB, begin2 + partB, k - partB);
		}
		else
		{
			return findKthSmallest(a, m - partA, begin1 + partA, b, n, begin, k - partA);
		}
	}
}