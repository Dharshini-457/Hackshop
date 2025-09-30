import pickle
import csv

# --------- Patient ADT ---------
class Patient:
    def _init_(self, pid, name, age, gender, diagnosis):
        self.id = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def _str_(self):
        return f"{self.id}\t{self.name:12}\t{self.age}\t{self.gender}\t{self.diagnosis}"


# --------- Stack ADT (Undo operations) ---------
class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


# --------- Queue ADT (Patient waiting list) ---------
class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


# --------- Tree ADT (Search patients by ID) ---------
class TreeNode:
    def _init_(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class PatientTree:
    def _init_(self):
        self.root = None

    def insert(self, patient):
        if self.root is None:
            self.root = TreeNode(patient)
        else:
            self._insert(self.root, patient)

    def _insert(self, node, patient):
        if patient.id < node.patient.id:
            if node.left is None:
                node.left = TreeNode(patient)
            else:
                self._insert(node.left, patient)
        elif patient.id > node.patient.id:
            if node.right is None:
                node.right = TreeNode(patient)
            else:
                self._insert(node.right, patient)

    def search(self, pid):
        return self._search(self.root, pid)

    def _search(self, node, pid):
        if node is None:
            return None
        if pid == node.patient.id:
            return node.patient
        elif pid < node.patient.id:
            return self._search(node.left, pid)
        else:
            return self._search(node.right, pid)


# --------- Patient List ADT ---------
class PatientList:
    def _init_(self):
        self.records = []
        self.undo_stack = Stack()
        self.waiting_queue = Queue()
        self.tree = PatientTree()

    def add_patient(self, pid, name, age, gender, diagnosis):
        if any(p.id == pid for p in self.records):
            return False
        patient = Patient(pid, name, age, gender, diagnosis)
        self.records.append(patient)
        self.undo_stack.push(("delete", patient))  # Store for undo
        self.waiting_queue.enqueue(patient)
        self.tree.insert(patient)
        return True

    def find_patient(self, pid):
        return self.tree.search(pid)

    def delete_patient(self, pid):
        for i, p in enumerate(self.records):
            if p.id == pid:
                self.undo_stack.push(("add", p))
                del self.records[i]
                return True
        return False

    def update_patient(self, pid, name=None, age=None, gender=None, diagnosis=None):
        p = self.find_patient(pid)
        if not p:
            return False
        old_data = Patient(p.id, p.name, p.age, p.gender, p.diagnosis)
        self.undo_stack.push(("update", old_data))
        if name is not None:
            p.name = name
        if age is not None:
            p.age = age
        if gender is not None:
            p.gender = gender
        if diagnosis is not None:
            p.diagnosis = diagnosis
        return True

    def display_all(self):
        if not self.records:
            print("No records.")
            return
        print("ID\tName\t\tAge\tG\tDiagnosis")
        print("-"*50)
        for p in self.records:
            print(p)

    def save_to_pickle(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.records, f)

    def load_from_pickle(self, filename):
        try:
            with open(filename, "rb") as f:
                self.records = pickle.load(f)
            for p in self.records:
                self.tree.insert(p)
        except FileNotFoundError:
            self.records = []

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Age", "Gender", "Diagnosis"])
            for p in self.records:
                writer.writerow([p.id, p.name, p.age, p.gender, p.diagnosis])


# --------- CLI ---------
def main():
    plist = PatientList()
    plist.load_from_pickle("patients.pkl")

    while True:
        print("\nPatient Record System with Stack, Queue, Tree")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Save (Pickle & CSV)")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pid = int(input("ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender (M/F/O): ").upper()
            diagnosis = input("Diagnosis: ")
            if plist.add_patient(pid, name, age, gender, diagnosis):
                print("Patient added.")
            else:
                print("ID already exists.")

        elif choice == "2":
            plist.display_all()

        elif choice == "3":
            pid = int(input("Enter ID to search: "))
            patient = plist.find_patient(pid)
            print(patient if patient else "Not found.")

        elif choice == "4":
            pid = int(input("Enter ID to update: "))
            p = plist.find_patient(pid)
            if not p:
                print("Not found.")
                continue
            name = input(f"New Name ({p.name}): ").strip() or None
            age_in = input(f"New Age ({p.age}): ").strip()
            age = int(age_in) if age_in else None
            gender = input(f"New Gender ({p.gender}): ").strip().upper() or None
            diagnosis = input(f"New Diagnosis ({p.diagnosis}): ").strip() or None
            plist.update_patient(pid, name, age, gender, diagnosis)
            print("Updated.")

        elif choice == "5":
            pid = int(input("Enter ID to delete: "))
            if plist.delete_patient(pid):
                print("Deleted.")
            else:
                print("Not found.")

        elif choice == "6":
            plist.save_to_pickle("patients.pkl")
            plist.save_to_csv("patients.csv")
            print("Saved to patients.pkl and patients.csv")

        elif choice == "0":
            plist.save_to_pickle("patients.pkl")
            plist.save_to_csv("patients.csv")
            print("Exit. Data saved.")
            break

        else:
            print("Invalid choice.")


if __name__== "_main_":
    main()