//import java.util.Scanner;
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
import javax.swing.*;
import java.awt.*;

public class main extends JFrame {
    public main() {
        setTitle("Hello Applet Replacement");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    public void paint(Graphics g) {
        super.paint(g);
        g.drawString("Hello Application!", 50, 100);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new main().setVisible(true);
        });
    }
}