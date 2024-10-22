/******************************************************************************

*******************************************************************************/
import java.util.Arrays;
public class Main
{
	public void merge(int[] arr, int start, int mid, int end) {
		int left = mid - start + 1;
		int right = end - mid;

		int[] leftArr = new int[left];
		int[] rightArr = new int[right];

		for (int i = 0; i < left; i++) {
			leftArr[i] = arr[start + i];
		}
		for (int j = 0; j < right; j++) {
			rightArr[j] = arr[mid + 1 + j];
		}

		int i = 0, j = 0;
		int k = start;
		while (i < left && j < right) {
			if (leftArr[i] <= rightArr[j]) {
				arr[k] = leftArr[i];
				i++;
			} else {
				arr[k] = rightArr[j];
				j++;
			}
			k++;
		}

		while (i < left) {
			arr[k] = leftArr[i];
			i++;
			k++;
		}
		while (j < right) {
			arr[k] = rightArr[j];
			j++;
			k++;
		}
	}

	public void mergeSort(int[] arr, int start, int end) {
		if (start < end) {
			int mid = (start + end) / 2;
			mergeSort(arr, start, mid);
			mergeSort(arr, mid + 1, end);
			merge(arr, start, mid, end);
		}
	}

	public boolean permutation(int[] array1, int[] array2) {
		if(array1.length != array2.length) return false;
		int i=0, j=0;
		while(i<array1.length && j<array2.length) {
			if(array1[i] != array2[j]) return false;
			i++;
			j++;
		}
		return true;
	}

	public static void main(String[] args) {
		int[] array1 = {1,2,3,4,5};
		int[] array2 = {5,1,2,3,4};

		Main obj = new Main();
		obj.mergeSort(array1, 0, array1.length-1);
		obj.mergeSort(array2, 0, array2.length-1);

		// System.out.println(Arrays.toString(array1));
		// System.out.println(Arrays.toString(array2));

		boolean result = obj.permutation(array1, array2);
		System.out.println(result);
	}
}