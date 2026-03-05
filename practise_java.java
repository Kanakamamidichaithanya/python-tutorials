class Student{
    String name;
    int age;
    int rollno;
    public void details{
        System.out.println("the student details are:")
        System.out.println("student name:",+ this.name)
        System.out.println("student age:",+ this.age)
        System.out.println("student rollno:", + this.rollno)
    }
}
public class oops{
    public static void main(String[] args){

    Student s1 = new Student();
    s1.name = "chaithanya";
    s1.age = 21;
    s1.rollno = 35;
    s1.details();
    }
}
