import java.util.*;
import java.io.*;
import java.util.List;


public class NweickTreeBuilderFromMESHstep2_reversing{
    public static void main(String[] args) throws IOException {

		Scanner input = new Scanner(new FileInputStream("C:\\Users\\Mahedi Hasan\\Desktop\\output7.txt")).useDelimiter(" ");
		PrintWriter writer = new PrintWriter("C:\\Users\\Mahedi Hasan\\Desktop\\output10.txt", "UTF-8");
		List<String> inverse = new ArrayList<String>();
		String nextToken="",tokenWrite="";
		while(input.hasNext()){
		nextToken= input.next();
		inverse.add(nextToken);
		//writer.print(nextToken);
		//System.out.println("Token:" +nextToken);
	}

	for(int i=inverse.size()-1;i>=0;i--){

		tokenWrite=inverse.get(i);
		//tokenWrite=tokenWrite.replaceAll("(",")");
		//tokenWrite=tokenWrite.replaceAll(")","(");
		//System.out.println("Token:" +tokenWrite);
		writer.print(tokenWrite);
	}
	//System.out.println(inverse.size());
	writer.close();
            }
}