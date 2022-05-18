package designpat.telephone;

public class Main{
    public static void main(String[] args) {
        final int NUM_DIGITS = 10;

        // Build the object graph
        PhoneModel PhoneModel = new PhoneModel(); //What's wrong?
        Screen screen = new Screen(PhoneModel);
        KeyPad keyPad = new KeyPad(PhoneModel);

        new FirstDigit(PhoneModel);
        
        enum Number{
        
        }

        // Run the program
        keyPad.simulateKeyPresses(NUM_DIGITS);

        //
        


    }
}
