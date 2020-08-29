import java.util.*;

public class Ejercicio1 {
    public static void main(String[] args) throws Exception {
        ImprimirPiramide(10);
    }
    
    public static void imprimirPiramide(int n) {
    """Función que imprime piramide de tamaño n
        parámetros:
        n : tamaño de la piramide"""
        
        int i = 1;
        while(i <= n) {
            int j = 1;
            while(j <= i) {
                System.out.print("*");
                j++;
            }
            System.out.println("");
            i++;
        }
        
    }
}