import employees
from employees.models import Employee
from employees.serializers import AddEmployeeSerializer, EmployeeDetailSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeesList(APIView):
    """
    List all employees or create a new employee
    """
    def get(self, request, format=None):
        snippets = Employee.objects.all()
        serializer = EmployeeDetailSerializer(snippets, many=True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = AddEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetails(APIView):
    """
    List an employee or delete an employee.
    """

    def get(self, request, id, format=None):

        try:
            employee = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"result": f"Employee not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)

    def delete(self, request, id, format=None):
        
        try:
            employee = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"result": f"Employee not found"},
                            status=status.HTTP_404_NOT_FOUND)

        employee_name = employee.name

        employee.delete()

        return Response({"result": f"Employee {employee_name} deleted!"},
            status=status.HTTP_200_OK)


   
