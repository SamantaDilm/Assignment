package designpat.telephone;

import java.util.ArrayList;
import java.util.List;

/**
 * Store a phone number, digit-by-digit
 */
public abstract class PhoneModel {
    public int Number;
    private List<Observer> digits = new ArrayList<Observer>();
    public abstract void update();

    public List<Observer> getDigits() {
        return digits;
    }
    //Do I need to do something with State?? --> yes

    public void addDigit(Observer newDigit) {
        digits.add(newDigit);
    }

    public int getNumber() {
        return Number;
    }
    
    public void setNumber(int Number) {
        this.Number = Number;
        notifyAllObservers();
    }

    public void notifyAllObservers(){
        for (Observer newDigit : digits)
        newDigit.update();
    }

}


