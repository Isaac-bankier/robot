//Main.cpp
//
//
//
//
//

int motor_strength(double Vlinear, double direction, double Vangular, int wheel) {
  double wheels[3] = [0.0, 120.0, 240.0]
  double wheelAngle = wheels[wheel]
  double Vrx = Vlinear * cos(direction);
  double Vry = Vlinear * sin(direction);
  double Vwx = Vrx * cos(wheelAngle);
  double Vwy = Vry * - sin(wheelAngle);
  double Vw = Vlinear * (cos(direction) * cos(wheelAngle) - sin(direction) * sin(wheelAngle)) + Vangular

}

void setup() {


}

void loop() {


}

void move_motor() {


}

void move_robot(direction, speed) {
  //direction is an int between -1 and 1
  //speed is a float between 0 and 1
  //
  //
  //
}

int get_ball(){


}
