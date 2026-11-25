using System;

class Greeter {
    public void SayHello() {
        Console.WriteLine("Привет! Добро пожаловать в программу.");
    }
}

internal static class Program {
    private static void Main() {
        Greeter greeter = new Greeter();
        greeter.SayHello();
    }
}