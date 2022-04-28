package designpat.telephone;

import java.util.Random;

/**
 * Mimic the data input ability of a physical phone's keypad;
 * however, here we're just sending it fake digits.
 */
public class KeyPad {
    private final PhoneModel model;

    public KeyPad(PhoneModel model) {
        this.model = model;
    }

    public void simulateKeyPresses(int numKeyPresses) {
        final int MAX_DIGIT = 10;
        Random rnd = new Random();
        for (int i = 0; i < numKeyPresses; i++) {
            int newDigit = rnd.nextInt(MAX_DIGIT);
            System.out.println("Pressing: " + newDigit);
            model.setNumber(newDigit); //Is this correct? it used to be:
            // addDigit(newDigit) but that didn't work out. Do you agree with this?
        }
    }

}
