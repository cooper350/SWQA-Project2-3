#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]) {
  if (argc != 4) {
    cerr << "Usage: " << argv[0] << " <height in feet> <height in inches> <weight in lbs>" << endl;
    return 1;
  }

  double height_ft = atof(argv[1]);
  double height_in = atof(argv[2]);
  double weight_lbs = atof(argv[3]);
  double bmi_score;
  string category;

  // Convert height to inches
  double height_total_inches = (height_ft * 12) + height_in;

  // Convert height to meters
  double height_m = height_total_inches * 0.0254;

  // Convert weight to kg
  double weight_kg = weight_lbs * 0.453592;

  // Calculate BMI score
  bmi_score = weight_kg / pow(height_m, 2);

  // Print out the BMI score
  cout << bmi_score << endl;

  return 0;
}
