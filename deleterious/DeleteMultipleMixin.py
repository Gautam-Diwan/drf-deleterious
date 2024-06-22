# Method which adds the ability to delete multiple model objects in a viewset
# based upon matching ids provided in request body.
# Endpoint is kept at "/" i.e same as list method of a viewset but can be overridden
# TODO: Add support for fields other than id
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import action


class DeleteMultipleMixin:
    # Default messages that can be overridden in subclasses
    invalid_body_message = "No {model_name}s provided"
    none_exist_message = "None of the provided {model_name}s exist"
    success_message = "Successfully deleted {count} {model_name}s"
    error_message = "Something went wrong: {error}"

    # default url path that can be overridden in subclasses
    delete_multiple_url_path = ""

    def __get_model_name(self):
        """
        The model name which is used to set url_name for reverse lookups
        and for JSON response messages of model name
        """
        return self.get_queryset().model._meta.model_name

    def __get_url_name(self):
        """
        url_name for reverse lookups
        """
        return f"delete_{self.__get_model_name()}"

    def initialize_action(self):
        """
        This method sets the URL name dynamically as per model name
        """
        delete_action = self.delete_multiple
        delete_action.url_name = self.__get_url_name()
        delete_action.url_path = self.delete_multiple_url_path
        self.delete_multiple = delete_action

    @action(
        detail=False,
        methods=["delete"],
        permission_classes=[permissions.IsAuthenticated],
        name="delete_multiple",
    )
    def delete(self, request, *args, **kwargs):
        """
        Method which adds the ability to delete multiple model objects in a viewset
        based upon matching ids provided in request body.
        Endpoint is kept at "/" i.e same as list method of a viewset
        """
        ids = request.data.get("ids", [])
        model_name = self.__get_model_name().capitalize()
        if not ids:
            return JsonResponse(
                {"error": self.invalid_body_message.format(model_name=model_name)},
                status=400,
            )

        try:
            model = self.get_queryset().model
            objects_to_delete = model.objects.filter(id__in=ids)
            if objects_to_delete.exists():
                count, _ = objects_to_delete.delete()
                return JsonResponse(
                    {
                        "message": self.success_message.format(
                            count=count, model_name=model_name
                        )
                    },
                    status=200,
                )
            return JsonResponse(
                {"error": self.none_exist_message.format(model_name=model_name)},
                status=400,
            )
        except Exception as error_message:
            return JsonResponse(
                {"error": self.error_message.format(error=error_message)}, status=400
            )