
# DRF Deleterious

DRF Deleterious is a simple mixin package for Django REST Framework which adds the ability to delete multiple requested entities in a single DELETE request.

## Features

- Delete multiple model objects based on matching IDs provided in the request body.
- Customizable success and error messages.
- Default endpoint is at "/", the same as the list method of a viewset, but can be overridden.

## Installation

Install the package using pip:

```sh
pip install drf-deleterious
```

## Requirements

- Python >= 3.8
- Django >= 4.0.2
- djangorestframework >= 3.14.0

## Usage

After installing the package, you can use the `DeleteMultipleMixin` in your Django REST Framework views.

### Basic Usage

```python
from deleterious import DeleteMultipleMixin
from rest_framework import viewsets
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelViewSet(DeleteMultipleMixin, viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

### Customizing Messages and URL Path

You can customize the messages and URL path by overriding the class attributes.

```python
class CustomDeleteMultipleViewSet(DeleteMultipleMixin, viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    # Custom messages
    invalid_body_message = "Please provide valid {model_name} IDs."
    none_exist_message = "None of the {model_name} IDs exist."
    success_message = "{count} {model_name}(s) were successfully deleted."
    error_message = "Error occurred: {error}"

    # Custom URL path
    delete_multiple_url_path = "delete-multiple"
```

## Example

Here is a more complete example of how to use `DeleteMultipleMixin` in a Django REST Framework viewset.

```python
from rest_framework import viewsets
from deleterious import DeleteMultipleMixin
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelViewSet(DeleteMultipleMixin, viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

In this example, `MyModelViewSet` will handle DELETE requests to delete multiple `MyModel` instances.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.
```

## Acknowledgements

Inspired by the needs of Django REST Framework users who require batch deletion functionality.
