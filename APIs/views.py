from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchQuerySerializer
from .utils import get_google_search_results, process_urls

class ScrapeView(APIView):
    def post(self, request):
        serializer = SearchQuerySerializer(data=request.data)
        
        if serializer.is_valid():
            query = serializer.validated_data['query']
            
            urls = get_google_search_results(query)
            
            summary = process_urls(urls) 

            return Response({"query": query, "summary": summary}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
