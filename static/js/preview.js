// Function to update the preview
function updatePreview(fieldId) {
    const input = document.getElementById(fieldId);
    const previewElement = document.getElementById(
      `preview${fieldId.charAt(0).toUpperCase() + fieldId.slice(1)}`
    );

    // Update the preview with the current input value
    previewElement.textContent = input.value || `Your ${fieldId}`;
  }

  function updatePreview() {
    const input = document.getElementById('image');
    const previewImage = document.getElementById('previewImage');
    
    if (input.files && input.files[0]) {
      const reader = new FileReader();

      reader.onload = function (e) {
        previewImage.src = e.target.result;
        previewImage.style.display = 'block';
      };

      reader.readAsDataURL(input.files[0]);
    } else {
      previewImage.style.display = 'none';
    }
  }