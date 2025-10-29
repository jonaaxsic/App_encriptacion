import hashlib
import base64

class CryptoAlgorithm:
    # ... (Resto de métodos y ENCRYPT sin cambios) ...

    @staticmethod
    def _generate_key_stream(key, length):
        """Genera un flujo de clave repetido"""
        key_stream = []
        for i in range(length):
            key_stream.append(ord(key[i % len(key)]))
        return key_stream
    
    @staticmethod
    def _calculate_checksum(data, key):
        """Calcula checksum para validación"""
        key_sum = sum(ord(c) for c in key)
        return (len(data) * key_sum) % 100
    
    @staticmethod
    def encrypt(text, key):
        """
        Encripta el texto usando algoritmo multicapa
        """
        if not text or not key:
            return None
        
        # Normalizar entrada
        text = text.upper()
        
        # CAPA 1: Sustitución polialfabética
        layer1 = ""
        key_stream = CryptoAlgorithm._generate_key_stream(key, len(text))
        
        for i, char in enumerate(text):
            if 'A' <= char <= 'Z':
                shift = key_stream[i]
                new_char = chr(((ord(char) - 65 + shift) % 26) + 65)
                layer1 += new_char
            elif char == ' ':
                layer1 += '|'
            else:
                layer1 += char
        
        # CAPA 2: Transposición matricial
        cols = int(len(layer1) ** 0.5) + 1
        rows = (len(layer1) + cols - 1) // cols
        
        matrix = []
        idx = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                if idx < len(layer1):
                    row.append(layer1[idx])
                    idx += 1
                else:
                    row.append('#')
            matrix.append(row)
        
        # Leer por columnas
        layer2 = ""
        for j in range(cols):
            for i in range(rows):
                layer2 += matrix[i][j]
        
        # CAPA 3: Conversión numérica con operaciones matemáticas
        key_seed = sum(ord(c) for c in key)
        layer3 = ""
        
        for i, char in enumerate(layer2):
            ascii_val = ord(char)
            key_mod = ord(key[i % len(key)])
            
            # XOR + multiplicación + offset
            value = ascii_val ^ key_mod
            value = (value * 13 + key_seed) % 100
            
            # Siempre 2 dígitos
            layer3 += str(value).zfill(2)
        
        # CAPA 4: Agregar metadatos y checksum
        checksum = CryptoAlgorithm._calculate_checksum(layer3, key)
        metadata = f"{checksum:02d}{cols:02d}{rows:02d}"
        
        return metadata + layer3
        
    @staticmethod
    def decrypt(encrypted_text, key):
        """
        Desencripta el texto usando algoritmo multicapa inverso
        """
        if not encrypted_text or not key or len(encrypted_text) < 6:
            return None
        
        try:
            # Extraer metadatos
            checksum = int(encrypted_text[0:2])
            cols = int(encrypted_text[2:4])
            rows = int(encrypted_text[4:6])
            numeric_data = encrypted_text[6:]
            
            # Validar checksum
            expected_checksum = CryptoAlgorithm._calculate_checksum(numeric_data, key)
            if checksum != expected_checksum:
                return "ERROR: Clave incorrecta o datos corruptos"
            
            # CAPA 3 INVERSA: Conversión numérica a caracteres (CORRECCIÓN CLAVE)
            key_seed = sum(ord(c) for c in key)
            layer2 = ""
            
            for i in range(0, len(numeric_data), 2):
                num_value = int(numeric_data[i:i+2])
                key_mod = ord(key[(i // 2) % len(key)])
                
                # --- CORRECCIÓN MATEMÁTICA: Reversión exacta ---
                
                # 1. Revertir la suma de key_seed
                temp_1 = (num_value - key_seed) % 100
                
                # 2. Revertir la multiplicación por 13 (multiplicar por el inverso 77)
                temp_2 = (temp_1 * 77) % 100 
                
                # 3. Revertir el XOR con key_mod para obtener el ASCII original
                ascii_val = temp_2 ^ key_mod
                
                # Usar el valor ASCII calculado
                layer2 += chr(ascii_val)

            # CAPA 2 INVERSA: Destransposición matricial
            matrix = [['' for _ in range(cols)] for _ in range(rows)]
            idx = 0
            
            for j in range(cols):
                for i in range(rows):
                    if idx < len(layer2):
                        matrix[i][j] = layer2[idx]
                        idx += 1
            
            # Leer por filas
            layer1 = ""
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] and matrix[i][j] != '#':
                        layer1 += matrix[i][j]
            
            # CAPA 1 INVERSA: Desustitución polialfabética
            key_stream = CryptoAlgorithm._generate_key_stream(key, len(layer1))
            result = ""
            
            for i, char in enumerate(layer1):
                if 'A' <= char <= 'Z':
                    shift = key_stream[i]
                    # CORRECCIÓN: Asegurar módulo positivo sumando 26
                    new_char = chr(((ord(char) - 65 - shift + 26) % 26) + 65) 
                    result += new_char
                elif char == '|':
                    result += ' '
                else:
                    result += char
            
            return result
            
        except Exception as e:
            return f"ERROR: {str(e)}"