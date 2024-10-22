/*
IsUnique / Contains Duplicate - LeetCode 217

Write a program to check if an array is unique or not.

Example

int[] intArray = {1,2,3,4,5,6};
isUnique(intArray) // true
*/

public class Main
{
	public static void main(String[] args) {
		int[] intArray = {1,2,3,4,5,6};

		for(int i=0; i<intArray.length; i++) {
			for(int j=i+1; j<intArray.length; j++) {
				if(intArray[i] == intArray[j]) {
					System.out.println(false);
				}
			}
		}

		System.out.println(true);
	}
}