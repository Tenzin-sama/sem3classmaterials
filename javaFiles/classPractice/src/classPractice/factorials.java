package classPractice;

public class factorials {

	public static void main(String[] args) {
		System.out.println("From Recursive:",fact(5));
		System.out.println(nonrecurFact(5));

	}
	public static int fact(int n) {
		// recursive function to get factorial of n
		if (n<=1) {
			return 1;
		}
		else {
			return n*fact(n-1);
		}
	}
	
	public static int nonrecurFact(int n) {
		/* This is an example of a multi-line comment
		 a linear function to get factorial of n
		 */
		if (n<=1) {
			return 1;
		}
		else {
			int facto=1;
			for (int i=1;i<=n;i++) {
				facto = facto*i;
			}
			return facto;
		}
	}

}
