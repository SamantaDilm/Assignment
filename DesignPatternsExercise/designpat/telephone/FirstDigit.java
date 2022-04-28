package designpat.telephone;

public class FirstDigit extends Observer {
    public FirstDigit(PhoneModel PhoneModel){
        this.PhoneModel = PhoneModel;
        this.PhoneModel.addDigit(this);
    }

    @Override
    public void update(){
        System.out.println("Pressing: " + PhoneModel.getDigits());
    }
}

    
