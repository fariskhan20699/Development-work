#include <iostream>
#include <vector>
using namespace std;
class Subject{
    private:
        string name;
        int creditHour;
        string grade;

    public:

        //constructer...
        Subject(string n,int ch,string g):name(n),creditHour(ch),grade(g){}

        //setters...
        void setName(string n){
            name = n;
        }

        void setCredit(int ch){
            creditHour = ch;
        }

        void setGrade(string g){
            grade = g;
        }

        //getters...
        string getName(){
            return name;
        }
        int getCredit(){
            return creditHour;
        }
        string getGrade(){
            return grade;
        }
        //allot the values defautl or contant values...
        double getGradePoints(){
            if(grade == "A"){
                return 4.0;
            }
            else if(grade == "A-"){
                return 3.67;
            }
            else if(grade == "B+"){
                return 3.33;
            }
            else if(grade == "B"){
                return 3.0;
            }
            else if(grade == "B-"){
                return 2.67;
            }
            else if(grade == "C+"){
                return 2.33;
            }
            else if(grade == "C"){
                return 2.0;
            }
            else if(grade == "C-"){
                return 1.67;
            }
            else if(grade == "D+"){
                return 1.33;
            }
            else if(grade == "D"){
                return 1.0;
            }
            else{
                return 0;
            }
        }
    };

class Student{
    private:
        string studentName;
        vector<Subject> subjects;
    public:
        //Students class constructor...
        Student(string name):studentName(name){}

        //getter...
        string getName(){
            return studentName;
        }

       //func. prototype...
        void addSubject(Subject subject){
            subjects.push_back(subject);
        }

        double calculateCGPA(){
            int totalCreditHours = 0;
            double totalGradePoints = 0.0;

            //using for each loop...
            for(Subject subject : subjects){
                totalGradePoints += subject.getCredit() * subject.getGradePoints();
                totalCreditHours += subject.getCredit();

            }

            if (totalCreditHours == 0)
            return 0;

            return totalGradePoints / totalCreditHours;

        }
        void displaySubjects(){
            cout<<"=====================================================\n";
            cout<<"***************** Finalized Result ******************\n";
            cout<<"=====================================================\n";

                for(Subject subject : subjects){
                     cout<<"Subject Name : "<<subject.getName()<<endl;
                     cout<<"Credit Hour : "<<subject.getCredit()<<endl;
                     cout<<"Grade : "<<subject.getGrade()<<endl;
                     cout<<"Grade Points : "<<subject.getGradePoints()<<endl;
                     cout<<"GPA:"<<subject.getCredit()*subject.getGradePoints()<<endl;

            cout<<"------------------------------------------------------\n";

        }
    }
    int getTotalCreditHours(){
        int totalCreditHours = 0;

        for(Subject subject : subjects){
            totalCreditHours += subject.getCredit();
        }

        return totalCreditHours;
    }
};

int main(){
    string name;
    int numberOfSubjects;

    cout<<"Enter the Student Name: ";
    getline(cin,name);
    Student student(name);

    cout<<"Enter the number of Subject: ";
    cin>>numberOfSubjects;

    for(int i=0;i<numberOfSubjects;i++){
        string subjectName;
        int creditHour;
        string grade;

        cout<<"\n Subject: "<<i+1<<endl;
        cin.ignore();

        cout<<"Enter the Subject Name: ";
        getline(cin,subjectName);

        cout<<"Enter the Credit Hours: ";
        cin>>creditHour;

        cout<<"Enter you Grade: ";
        cin>>grade;

        Subject subject(subjectName,creditHour,grade);
        student.addSubject(subject);
    }
    student.displaySubjects();
    double gpa = student.calculateCGPA();

    if(gpa >= 3.75)
    {
        cout<<"\033[36m";

        cout<<"\n================================"<<endl;
        cout<<"           RESULT                "<<endl;
        cout<<"================================="<<endl;

        cout<<"Student Name: "<<student.getName()<<endl;
        cout<<"Total Credit Hours: "<<student.getTotalCreditHours()<<endl;
        cout<<"Total GPA: "<<student.calculateCGPA()<<endl;

        cout<<"\nCongratulations!"<<endl;
        cout<<"You are eligible for scholarship."<<endl;

        cout<<"================================"<<endl;
        cout<<"\033[0m";
    }

    else if(gpa >= 3.5)
    {
        cout<<"\033[32m";

        cout<<"\n================================"<<endl;
        cout<<"           RESULT                 "<<endl;
        cout<<"================================="<<endl;

        cout<<"Student Name: "<<student.getName()<<endl;

        cout<<"Total Credit Hours: "<<student.getTotalCreditHours()<<endl;
        cout<<"Total GPA: "<<student.calculateCGPA()<<endl;
        cout<<"GPA: "<<gpa<<endl;
        cout<<"\nCongratulations!"<<endl;
        cout<<"You are eligible for scholarship."<<endl;

        cout<<"================================"<<endl;
        cout<<"\033[0m";
    }
    else if(gpa >= 2.0){
        cout<<"\033[34m";

        cout<<"\n================================"<<endl;
        cout<<"           RESULT                 "<<endl;
        cout<<"================================="<<endl;

        cout<<"Student Name: "<<student.getName()<<endl;
        cout<<"Total GPA: "<<student.calculateCGPA()<<endl;
        cout<<"Total Credit Hours: "<<student.getTotalCreditHours()<<endl;

        cout<<"\nKeep It up"<<endl;
        cout<<"For better Result Good Wishes..."<<endl;

        cout<<"================================"<<endl;
        cout<<"\033[0m";
    }
    else{
        cout<<"\033[31m";

        cout<<"\n===================================="<<endl;
        cout<<"           RESULT                   "<<endl;
        cout<<"===================================="<<endl;

        cout<<"Student Name: "<<student.getName()<<endl;
        cout<<"Total GPA: "<<student.calculateCGPA()<<endl;
        cout<<"Total Credit Hours: "<<student.getTotalCreditHours()<<endl;

        cout<<"\n!!!Please:"<<endl;
        cout<<"improve your academic performance!!!"<<endl;

        cout<<"===================================="<<endl;
        cout<<"\033[0m";
        }
return 0;
}
