# import time
# start = time.perf_counter()  # time.per_counter has higher precision than time.time() so here we hve used this

# def test_func():
#     print("Working")
#     print("Sleep for 1 sec")
#     time.sleep(1)
#     print("Sleeping Completed")

# test_func()
# test_func()
# test_func()
# end = time.perf_counter()

# print(f"The Program finshes in {round(end-start, 2)} seconds")


# import multiprocessing
# import time

# def test_func():
#     print("Working")
#     print("Sleep for 1 sec")
#     time.sleep(1)
#     print("Sleeping Completed")

# if __name__ == "__main__":
#     start = time.perf_counter()  # time.per_counter has higher precision than time.time() so here we hve used this

#     p1 = multiprocessing.Process(target = test_func)
#     p2 = multiprocessing.Process(target = test_func)
    
#     p1.start()
#     p2.start()
    
#     p1.join()
#     p2.join()
    
#     end = time.perf_counter()
    
#     print(f"The Program finshes in {round(end-start, 2)} seconds")


# import multiprocessing
# import concurrent.futures
# import time

# def test_func():
#     print("Working")
#     print("Sleep for 1 sec")
#     time.sleep(1)
#     print("Sleeping Completed")

# if __name__ == "__main__":
#     start = time.perf_counter()  # time.per_counter has higher precision than time.time() so here we hve used this

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(test_func, range(10))
    
#     end = time.perf_counter()
    
#     print(f"The Program finshes in {round(end-start, 2)} seconds")



# import multiprocessing
# import time

# def test_func():
#     print("Working")
#     print("Sleep for 1 sec")
#     time.sleep(1)
#     print("Sleeping Completed")

# if __name__ == "__main__":
#     start = time.perf_counter()  # time.per_counter has higher precision than time.time() so here we hve used this

#     processess = []  # Create a List to store all process objects
#     for i in range(10):
#         p = multiprocessing.Process(target = test_func)  # Create instance of test_func
#         p.start()  # Start Process
#         processess.append(p)  # Append processess

#     for process in processess:  # Perform Join Operations
#         process.join()

#     end = time.perf_counter()

#     print(f"The Program finshes in {round(end-start, 2)} seconds")


# import multiprocessing
# import time

# def square(index,value):
#     value[index] = value[index] ** 2

# arr = multiprocessing.Array('i', [1,2,3,4,5])

# if __name__ == "__main__":
#     start = time.perf_counter()  # time.per_counter has higher precision than time.time() so here we hve used this

#     processess = []  # Create a List to store all process objects
#     for i in range(5):
#         p = multiprocessing.Process(target = square, args = (i, arr))  # Create instance of test_func
#         p.start()  # Start Process
#         processess.append(p)  # Append processess

#     for process in processess:  # Perform Join Operations
#         process.join()

#     print(f"The Square of all number in the list: {list(arr)}")
#     end = time.perf_counter()

#     print(f"The Program finshes in {round(end-start, 2)} seconds")


import multiprocessing
import time

def square(no):
    return no * no

if __name__ == "__main__":
    start = time.perf_counter()
    numbers = [2, 4, 6, 8]

    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)

    print(results)

    end = time.perf_counter()
    print(f"The Program finshes in {round(end-start, 2)} seconds")


import multiprocessing

def enroll_students(student_queue):
    for student in ["Aashish", "Karan", "Nakul", "Kabir"]:
        student_queue.put(f"enroll {student}")  # Enroll each student one by one in the student_queue

    student_queue.put(None)

def register_students(student_queue):   # Now Register those Students 
    while True:
        enrollment_req = student_queue.get()
        if enrollment_req is None:
            break
        print(f"Registrar: {enrollment_req}")

if __name__ == "__main__":
        student_queue = multiprocessing.Queue()
        enroll_process = multiprocessing.Process(target = enroll_students, args = (student_queue,))
        reg_process = multiprocessing.Process(target = register_students, args = (student_queue,))

        enroll_process.start()
        reg_process.start()

        enroll_process.join()
        reg_process.join()