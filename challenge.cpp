// This file is here to let you practice with merge errors.
#include <string>
#include <iostream>

class Chair {
 private:
  int height_cm;
  int amount_of_legs;
  std::string chair_name;
 public:
  chair(int height, int legs_amount, std::string name){
    height_cm(height),
    amount_of_legs(legs_amount),
    chair_name(name)
  }
  void print_data(){
   std::cout << "name of chair: " << chair_name << "\n";
   std::cout << "Height in cm: " << height_cm << "\n";
   std::cout << "amount of legs; " << amount_of_legs << std::endl;
  }
}

int main(){
  Chair chair = Chair(5, 4, "hugo");
  std::cout << "printing data..." << std::endl;
  chair.print_data();
}
