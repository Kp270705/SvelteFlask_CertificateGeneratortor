# list1 = ["Rahul", "Neha", "Kirti", "Ravi", "Deepak", "Vipin", "Himani", "Suresh"]

# for i, name in enumerate(list1, start=1):
#     # print(f"{i}. {name}")
#     pass

# print(f"{enumerate(list1, start=1)}")


# ===============================


class Solution:
    def testm1(self, arg1, arg2, arg3):
        print(f"test-m1.")
    def testm2(self, arg1, arg2, arg3):
        print(f"test-m2.")
    def testm3(self, arg1, arg2, arg3):
        print(f"test-m3.")

def testDict():
    pass


def getData():
    sol = Solution()
    certChoice = {
        f"Choice1": sol.testm1,
        f"Choice2": sol.testm2,
        f"Choice3": sol.testm3,
    }
    bla_bla_args = []
    for i in range(1, 4):
        bla_bla_args = ["arg1", "arg2", "arg3"]
        certChoice[f"Choice{i}"](*bla_bla_args)
        # print(f"Choice{i} is called.")
