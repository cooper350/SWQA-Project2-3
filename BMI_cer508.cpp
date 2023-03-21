#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main() {
    double height_ft, height_in, weight_lbs, bmi_score;
    string category; 

    cout << "Hello, welcome to the BMI calculator!" << endl;


    cout << "How Many feet tall are you?  ";
    cin >> height_ft;
    cout << "How Many inches?  ";
    cin >> height_in;

    // Convert height to inches
    double height_total_inches = (height_ft * 12) + height_in;

    // Take user input for weight in pounds
    cout << "How much do you weigh?  ";
    cin >> weight_lbs;

    // Calculate BMI score
    bmi_score = (weight_lbs * 703) / pow(height_total_inches, 2);

    if (bmi_score < 18.5)
    {
        category = "Underweight";
    }

    else if (bmi_score >= 18.5)
    {
        if (bmi_score <= 24.9)
        {
        category = "Normal Weight";
        } 

        else if (bmi_score >= 25)
        {
            if (bmi_score >= 30)
            {
                category = "Obese";
            }
            else
            {
            category = "Overweight";
            }

        }

    }

    // Print out the BMI score
    cout << "your BMI Score is: " << bmi_score << endl;
    cout << "meaning that you are " << category << endl;

    return 0;
}
