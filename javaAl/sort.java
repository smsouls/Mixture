public class Selection {
	public static void sort(Comparable[] a) {
		int N = a.length;
		for (i = 0; i < N; i++) {
			int min = i;
			for (j = i + 1; j < N; j++) {
				if(less(a[j], a[min])) {
					min = j;
				}
				exch(a, i, min)
			}
		}
	}
}


public class Insertion {
	public static void sort(Comparable[] a) {
		int N = a.length;
		for (int i = 1; i < N; i++) {
			for (int j = i; j > 0 && less(a[j], a[j-1]); j--) {
				exch(a, j, j-1)
			}
		}
	}
}



//希尔排序是插入排序的改进，插入排序是相邻之间的互换，而希尔排序则是相邻一段的互换
public class Shell {
	public static void sort(Comparable[] a) {
		int N = a.length;
		int h = 1;
		while(h < N/3) {
			h = 3 * h + 1;  //分为这么多的组
		}
		while(h >= 1) {
			for (int i = h; i < N; i++) {
				for (int j = i; j >= h && less(a[j], a[j-h]); j -= h) {
					exch(a, j, j-h);
				}
				h = h/3;
			}
		}
	}
}