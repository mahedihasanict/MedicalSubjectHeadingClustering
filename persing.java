/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package parser;

import com.mysql.jdbc.Connection;
import com.mysql.jdbc.Statement;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author Миша
 */
public class Parser {

    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost/ahsumed87";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123";

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, ClassNotFoundException, SQLException {
        Connection conn = null;
        Statement stmt = null;
        File file = new File("C:\\ohsumed.87");
        Scanner input = new Scanner(file);

        //STEP 3: Open a connection
        System.out.println("Connecting to a selected database...");

        System.out.println("Connected database successfully...");

        //STEP 4: Execute a query
        System.out.println("Inserting records into the table...");

        int s = 0, m = 0, t = 0, p = 0, w = 0, a = 0;
        String U = "", S = "", M = "", T = "", P = "JOURNAL ARTICLE.", W = "", A = "";
        ArrayList<String> u = new ArrayList<String>();
        while (input.hasNext()) {

            String nextToken = input.next();
            if (nextToken.equals(".U")) {
                U = input.next();
            }
            
            if (nextToken.equals(".S")) {
                s = 1;
                S = S + " " + input.next();

            } else if (s == 1) {
                if (nextToken.equals(".M")) {
                    s = 0;
                    //System.out.println(".S=  " + S);
                    S = S.replaceAll("'", "");
                } else {
                    S = S + " " + nextToken;

                }
            }
            if (nextToken.equals(".M")) {
                m = 1;
                M = M + " " + input.next();

            } else if (m == 1) {
                if (nextToken.equals(".T")) {
                    m = 0;
                    //  System.out.println(".M=  " + M);
                    M = M.replaceAll("'", "");
                } else {
                    M = M + " " + nextToken;

                }
            }

            if (nextToken.equals(".T")) {
                t = 1;
                T = T + " " + input.next();

            } else if (t == 1) {
                if (nextToken.equals(".P")) {
                    t = 0;
                    //System.out.println(".T=  " + T);
                    T = T.replaceAll("'", "");
                } else {
                    T = T + " " + nextToken;

                }
            }

//            if (nextToken.equals(".P")) {
//                p = 1;
//                P = P + " " + input.next();
//
//            } else if (p == 1) {
//                if (nextToken.equals(".W")) {
//                    p = 0;
//                    //System.out.println(".P=  " + P);
//
//                } else {
//                    P = P + " " + nextToken;
//
//                }
//            }
            if (nextToken.equals(".W")) {
                w = 1;
                W = W + " " + input.next();

            } else if (w == 1) {
                if (nextToken.equals(".A")) {
                    w = 0;
                    W = W.replaceAll("'", "");
                    //System.out.println(".W=  " + W);

                } else {
                    W = W + " " + nextToken;

                }
            }
            if (nextToken.equals(".A")) {
                a = 1;
                A = A + " " + input.next();

            } else if (a == 1) {
                if (nextToken.equals(".I")) {
                    a = 0;
                    A = A.replaceAll("'", "");
                    System.out.println(".U=  " + U);
                    System.out.println(".S=  " + S);
                    System.out.println(".M=  " + M);
                    System.out.println(".T=  " + T);
                    System.out.println(".P=  " + P);
                    System.out.println(".W=  " + W);
                    System.out.println(".A=  " + A);
                    Class.forName("com.mysql.jdbc.Driver");
                    conn = (Connection) DriverManager.getConnection(DB_URL, USER, PASS);
                    stmt = (Statement) conn.createStatement();
                    String sql = "INSERT INTO med1 "
                            + "("
                            + " u"
                            + " ,s"
                            + " ,m"
                            + " ,t"
                            + " ,p"
                            + " ,w"
                            + " ,a"
                            + ")"
                            + "VALUES"
                            + "("
                            + " '" + U + "'"
                            + " ,'" + S + "' "
                            + " ,'" + M + "' "
                            + " ,'" + T + "'"
                            + " ,'" + P + "' "
                            + " ,'" + W + "'"
                            + " ,'" + A + "'"
                            + ")";
                    stmt.executeUpdate(sql);
                    U = "";
                    S = "";
                    M = "";
                    T = "";
                    //P = "";
                    W = "";
                    A = "";
                } else {
                    A = A + " " + nextToken;

                }

            }

//            if (u == 1) {
//                System.out.println(".U " + nextToken);
//                u = 0;
//            }
//
//            if (nextToken.equals(".S") || s == 1) {
//                if (nextToken.equals(".S")) {
//                    System.out.println(".S " + input.next());
//                    s = 1;
//                } else if (s == 1) {
//                    if (nextToken.equals(".M")) {
//                        s = 0;
//                        m = 1;
//                    } else {
//                        System.out.println(".S " + nextToken);
//                    }
//                }
//
//            }
//
//            if (nextToken.equals(".M") || m == 1) {
//                if (nextToken.equals(".M")) {
//                    System.out.println(".M " + input.next());
//                    m = 1;
//                } else if (s == 1) {
//                    if (nextToken.equals(".T")) {
//                        m = 0;
//                        t = 1;
//                    } else {
//                        System.out.println(".M " + nextToken);
//                    }
//                }
//
//            }
//
//            if (nextToken.equals(".T") || t == 1) {
//                if (nextToken.equals(".T")) {
//                    System.out.println(".T " + input.next());
//                    t = 1;
//                } else if (s == 1) {
//                    if (nextToken.equals(".P")) {
//                        t = 0;
//                        p = 1;
//                    } else {
//                        System.out.println(".T" + nextToken);
//                    }
//                }
//
//            }
//            if (nextToken.equals(".P") || p == 1) {
//                if (nextToken.equals(".P")) {
//                    System.out.println(".P " + input.next());
//                    t = 1;
//                } else if (s == 1) {
//                    if (nextToken.equals(".W")) {
//                        t = 0;
//                        w = 1;
//                    } else {
//                        System.out.println(".P" + nextToken);
//                    }
//                }
//
//            }
//
//            if (nextToken.equals(".W") || w == 1) {
//                if (nextToken.equals(".W")) {
//                    System.out.println(".W " + input.next());
//                    t = 1;
//                } else if (s == 1) {
//                    if (nextToken.equals(".A")) {
//                        w = 0;
//                        a = 1;
//                    } else {
//                        System.out.println(".W" + nextToken);
//                    }
//                }
//
//            }
//
//            if (nextToken.equals(".A") || a == 1) {
//                if (nextToken.equals(".A")) {
//                    System.out.println(".A " + input.next());
//                    t = 1;
//                } else if (s == 1) {
//                    if (nextToken.equals(".U")) {
//                        a = 0;
//                        u = 1;
//                    } else {
//                        System.out.println(".A" + nextToken);
//                    }
//                }
//
//            }
//application logic here
        }
//        for (int i = 0; i < u.size(); i++) {
//            System.out.println(u.get(i));
//        }
        input.close();

    }
}
