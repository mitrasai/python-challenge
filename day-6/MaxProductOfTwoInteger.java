/******************************************************************************
Max Product of Two Integers

How to find maximum product of two integers in the array where all elements are positive.

Example

int[] intArray = {10,20,30,40,50};
maxProduct(intArray) // (40,50)

*******************************************************************************/

public class Main
{
	public static String maxProduct(int[] intArray) {
		int n = intArray.length;
		int prodMaxi = 0;
		String maxiPair = "";

		for(int i=0; i<n; i++) {
			for(int j=i+1; j<n; j++) {
				int product = intArray[i] * intArray[j];
				if(product > prodMaxi) {
					prodMaxi = product;
					maxiPair = "("+intArray[i]+", "+intArray[j]+")";
				}
			}
		}
		return maxiPair;
	}

	public static void main(String[] args) {
		int[] intArray = {10,20,30,40,50};
		String result = maxProduct(intArray);
		System.out.println(result);
	}
}