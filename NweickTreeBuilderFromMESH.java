import java.sql.*;
import java.util.*;
import java.io.*;
//import java.sql.Connection;
//import java.sql.DatabaseMetaData;
//import java.sql.DriverManager;
//import java.sql.ResultSet;
//import java.sql.SQLException;

public class NweickTreeBuilderFromMESH{
    public static void main(String[] args) throws IOException, SQLException {
        Connection conn = null;
        ResultSet rs = null;
        String url = "jdbc:sqlserver://127.0.0.1;instance=MSSQLSERVER;DatabaseName=Medline";
        String driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver";
        String userName = "sa";
        String password = "0000";
        Statement stmt = null;

        PrintWriter writer = new PrintWriter("C:\\Users\\Mahedi Hasan\\Desktop\\output7.txt", "UTF-8");

        try {
            Class.forName(driver);
            conn = DriverManager.getConnection(url, userName, password);
            stmt = conn.createStatement();
            System.out.println("Connected to the database..");
            String sql = "SELECT [MESH_TREE_NUMBER] FROM [Medline].[dbo].[AsciiDescriptorTreebased]  where MESH_TREE_NUMBER like' Z%' group by [MESH_TREE_NUMBER];";
            rs=stmt.executeQuery(sql);

            ResultSetMetaData rsmd = rs.getMetaData();
            int columnsNumber = rsmd.getColumnCount();
            //rs.first();
            //rs.next();
            /*rs.next();
            rs.next();
                  String mesh_heading = rs.getString(1);
                  String tree_number = rs.getString(2);*/
			      //String last = rs.getString(2);
				String columnValuePrev="";
				int z=0,n=0;
				writer.print("Z;");
			    while (rs.next()) {
					//System.out.print("(");
						n++;

			        for (int i = 1; i <= columnsNumber; i++) {
			            //if (i > 1) System.out.print(":");
			            String columnValue = rs.getString(i);
			            columnValue=columnValue.replaceAll(" ","");

			            //String columnValue = rs.first(1);
			            if(columnValuePrev.length()<columnValue.length()){
							//if (n > 1) System.out.print(",");
							//if (n > 1) writer.print(",");
							//System.out.print("(");
							writer.print(" "+")"+" ");
							z++;
						}

						if(columnValuePrev.length()>columnValue.length()){
							int x=(columnValuePrev.length()-columnValue.length())/4;
							for(int j=1;j<=x;j++){
							//System.out.print(")");
							writer.print(" "+"(");
							z--;}
							writer.print(" "+","+" ");
						}

						if(columnValuePrev.length()==columnValue.length())
							//System.out.print(",");
							writer.print(" "+","+" ");

			            //System.out.print(columnValue);
			            writer.print(columnValue);
			            columnValuePrev=columnValue;

			            //+ " " + rsmd.getColumnName(i));
			        }
			        //System.out.print(")");
			        //System.out.println("");
    }
    for(int k=1;k<=z;k++)
	//System.out.print(")");
	writer.print(" "+"(");
			//System.out.println(mesh_heading+""+tree_number);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            conn.close();
            rs.close();
            writer.close();
        }
    }
}