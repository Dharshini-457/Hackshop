import java.util.Scanner;
/*class main{
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        int num=input.nextInt();
        int sum=0;
        System.out.print("Reversed number: ");
        while(num>0){
            int n=num%10;
            System.out.print(n);
            sum=sum+n;
            num=num/10;
        }
        System.out.println("\nSum of digits: "+sum);
    }
}*/
import java.applet.Applet;
import java.awt.Graphics;

// HelloWorld class extends Applet
public class main extends Applet {
    
    // Overriding paint() method
    @Override public void paint(Graphics g)
    {
        g.drawString("Hello World", 20, 20);
    }
}