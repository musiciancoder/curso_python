#SIN LAMBDA EXPRESSION

animals1 = ["Dog","cat","ELEPHANT","Badger"]

animals2 = map(str.lower, animals1)

print(list(animals2))

"""
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LowerCaseExample {
    public static void main(String[] args) {
        List<String> animals1 = Arrays.asList("Dog", "cat", "ELEPHANT", "Badger");

        List<String> animals2 = animals1.stream()
                                        .map(String::toLowerCase) // Convert each string to lowercase
                                        .collect(Collectors.toList());

        System.out.println(animals2);
    }
}

"""

print

#CON LAMBDA EXPRESSION

animals3 = ["Dog","cat","ELEPHANT","Badger"]

animals4 = map(lambda  s: s[:3], animals3) #las 3 primeras letras

print(list(animals4))

"""
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class SubstringExample {
    public static void main(String[] args) {
        List<String> animals3 = Arrays.asList("Dog", "cat", "ELEPHANT", "Badger");

        List<String> animals4 = animals3.stream()
                                        .map(s -> s.substring(0, Math.min(3, s.length()))) // Extract first 3 chars
                                        .collect(Collectors.toList());

        System.out.println(animals4);
    }
}

"""