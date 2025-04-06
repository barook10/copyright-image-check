<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div id="app">
    <div class="container">
      <h1>Copyright Image Check</h1>
      <div class="upload-section">
        <input type="file" @change="handleFileUpload" accept="image/*" ref="fileInput">
        <button @click="uploadImage">Check Copyright</button>
      </div>
      
      <div v-if="isLoading" class="loading">Processing image...</div>
      
      <div v-if="result" class="result-section">
        <h2>Results</h2>
        <div class="image-preview">
          <img :src="imagePreview" alt="Uploaded image">
        </div>
        <div class="verdict" :class="{'infringed': result.verdict === 'Copyright Infringed'}">
          {{ result.verdict }}
        </div>
        <div class="confidence">
          Confidence: {{ result.confidence }}%
        </div>
      </div>
      
      <div v-if="error" class="error">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      selectedFile: null,
      imagePreview: null,
      isLoading: false,
      result: null,
      error: null
    }
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
      this.previewImage();
      this.result = null;
      this.error = null;
    },
    previewImage() {
      if (!this.selectedFile) return;
      
      const reader = new FileReader();
      reader.onload = (e) => {
        this.imagePreview = e.target.result;
      };
      reader.readAsDataURL(this.selectedFile);
    },
    async uploadImage() {
      if (!this.selectedFile) {
        this.error = 'Please select an image first';
        return;
      }
      
      this.isLoading = true;
      this.error = null;
      
      try {
        const formData = new FormData();
        formData.append('file', this.selectedFile);

        const response = await fetch('http://127.0.0.1:5000/check_copyright', {
          method: 'POST',
          body: formData
        });
        
        const data = await response.json();
        
        if (!response.ok) {
          throw new Error(data.error || 'Failed to process image');
        }

        this.result = data;
        this.imagePreview = `http://127.0.0.1:5000/uploads/${data.file_id}`;
      } catch (err) {
        this.error = err.message;
        console.error('Upload error:', err);
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>

<style>
/* Basic Reset */
body {
  margin: 0;
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* Container */
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

/* Headers */
h1 {
  color: #333;
  text-align: center;
}

/* Upload Section */
.upload-section {
  margin: 30px 0;
  text-align: center;
}

input[type="file"] {
  margin-bottom: 10px;
}

button {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #45a049;
}

/* Results */
.result-section {
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.image-preview img {
  max-width: 100%;
  max-height: 300px;
  margin: 10px 0;
}

.verdict {
  font-weight: bold;
  margin: 10px 0;
  color: #4CAF50;
}

.verdict.infringed {
  color: #f44336;
}

/* Loading and Error States */
.loading {
  color: #666;
  font-style: italic;
}

.error {
  color: #f44336;
  margin: 10px 0;
}
</style>