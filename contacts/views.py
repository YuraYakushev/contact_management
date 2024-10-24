from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
import requests



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def check_ip_region(self):
        user_ip = self.request.META.get('REMOTE_ADDR')
        print(f"User IP: {user_ip}")

        # Allow access for local requests
        if user_ip in ['127.0.0.1', '::1']:
            return True

        try:
            response = requests.get(f'https://ipapi.co/{user_ip}/json/')
            data = response.json()
            print(f"Country data: {data}")

            # Check if the country is allowed
            if data.get('country') not in ['UA', 'PL']:
                return False
        except Exception as e:
            print(f"Error fetching country data: {e}")
            return False

        return True

    def list(self, request, *args, **kwargs):
        if not self.check_ip_region():
            return Response({"detail": "Forbidden."}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not self.check_ip_region():
            return Response({"detail": "Forbidden."}, status=status.HTTP_403_FORBIDDEN)

        print(f"Request data: {request.data}")
        if not request.user.is_authenticated:
            print("User is not authenticated.")
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        # Getting query parameters
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')

        if first_name:
            queryset = queryset.filter(first_name__istartswith=first_name)
            print(f"Filtered queryset by first_name: {queryset}")

        if last_name:
            queryset = queryset.filter(last_name__istartswith=last_name)
            print(f"Filtered queryset by last_name: {queryset}")

        return queryset

    def update(self, request, *args, **kwargs):
        if not self.check_ip_region():
            return Response({"detail": "Forbidden."}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not self.check_ip_region():
            return Response({"detail": "Forbidden."}, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)