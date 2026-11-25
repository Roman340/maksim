using System;

class Greeter {
    public void SayHello() {
        Console.WriteLine("Привет, мир!");
    }
}

class Program {
    static void Main() {
        Greeter greeter = new Greeter();
        greeter.SayHello();
    }
}