package oop.school;

// Using record is very good when:
//   Dealing with database
//   Dealing with immutable data
public record LPAStudent(String id, String name, String dateOfBirth, String classList) {
}
