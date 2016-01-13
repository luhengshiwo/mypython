package callpython;
import java.io.BufferedReader;  
import java.io.InputStreamReader;   
public class Luhengusejavacallpython {  
        public static void main(String[] args){  
                try{  
                        System.out.println("start");  
                        Process pr = Runtime.getRuntime().exec("python D:\\luheng\\mypython\\test.py 22");  
                        BufferedReader in = new BufferedReader(new  
                                InputStreamReader(pr.getInputStream()));  
                        String line; 
                        while ((line = in.readLine()) != null) {  
                        	String a = line ;
                            System.out.println(a);  
                        }  
                        in.close();  
                        pr.waitFor();  
                        System.out.println("end");  
                } catch (Exception e){  
                            e.printStackTrace();  
                        }  
                }  
}