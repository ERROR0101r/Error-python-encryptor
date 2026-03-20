#!/usr/bin/env python3

import os
import sys
import json
import random
import hashlib
import argparse
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

VERSION = "1.0"
DEVELOPER = "@ERROR0101risback"
CHANNEL = "https://t.me/aab_ho_ga_comeback"

class ERRORHTMLEncryptor:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.NIBBLE_CHARS = ["😈", "👾", "🤖", "💀", "🎭", "🔮", "⚡", "🔥", 
                           "❄️", "🌈", "🍕", "🚀", "💎", "🎯", "⭐", "🌙"]
        
        self.NOISE_CHUNKS = [
            "🔒 ERROR PROTECTION ACTIVE 🔒",
            "😈 ERROR SECURITY LAYER 😈",
            "⚡ ENCRYPTION ENGINE ONLINE ⚡",
            "🔥 ANTI-TAMPER MODE 🔥",
            "💀 REVERSE PROTECTION 💀",
            "🎭 CODE OBFUSCATION 🎭",
            "🔑 KEY EXTRACTION 🔑",
            "ERROR CHECKSUM VERIFIED",
            "PROTECTED BY @ERROR0101risback",
            "CHANNEL: https://t.me/aab_ho_ga_comeback",
            "❌ ERROR ENCRYPTION ACTIVE ❌",
            "⚠️ UNAUTHORIZED ACCESS DENIED ⚠️",
            "🔒 MILITARY GRADE ENCRYPTION 🔒",
            "💀 ERROR PROTECTION LAYER 💀"
        ]
        
        self.log("ERROR HTML Encryptor initialized")
    
    def log(self, message):
        if self.verbose:
            print(f"[LOG] {message}")
    
    def quick_noise(self, count=6):
        noise = []
        for i in range(count):
            chunk = random.choice(self.NOISE_CHUNKS)
            extra = ''.join(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?") for _ in range(10))
            noise.append(f"{chunk} {extra}")
        return noise
    
    def bytes_to_hex_nibbles(self, data):
        hex_str = data.hex()
        translation = {
            '0': self.NIBBLE_CHARS[0], '1': self.NIBBLE_CHARS[1],
            '2': self.NIBBLE_CHARS[2], '3': self.NIBBLE_CHARS[3],
            '4': self.NIBBLE_CHARS[4], '5': self.NIBBLE_CHARS[5],
            '6': self.NIBBLE_CHARS[6], '7': self.NIBBLE_CHARS[7],
            '8': self.NIBBLE_CHARS[8], '9': self.NIBBLE_CHARS[9],
            'a': self.NIBBLE_CHARS[10], 'b': self.NIBBLE_CHARS[11],
            'c': self.NIBBLE_CHARS[12], 'd': self.NIBBLE_CHARS[13],
            'e': self.NIBBLE_CHARS[14], 'f': self.NIBBLE_CHARS[15]
        }
        return ''.join(translation.get(c.lower(), c) for c in hex_str)
    
    def encrypt_content_fast(self, content):
        key = get_random_bytes(32)
        iv = get_random_bytes(12)
        
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
        ciphertext, tag = cipher.encrypt_and_digest(pad(content.encode('utf-8'), AES.block_size))
        
        encrypted_data = ciphertext + tag
        checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        return {
            'key': key.hex(),
            'iv': iv.hex(),
            'encrypted': encrypted_data.hex(),
            'checksum': checksum
        }
    
    def split_fragments_fast(self, nibble_str, n=6):
        frag_size = len(nibble_str) // n
        return [nibble_str[i*frag_size:(i+1)*frag_size] for i in range(n-1)] + \
               [nibble_str[(n-1)*frag_size:]]
    
    def hide_key_in_noise_fast(self, key_hex, n=6):
        part_len = len(key_hex) // n
        key_parts = [key_hex[i*part_len:(i+1)*part_len] for i in range(n-1)] + \
                    [key_hex[(n-1)*part_len:]]
        
        noise_list = []
        for i, part in enumerate(key_parts):
            padding = random.randint(1, 3)
            rot = random.randint(0, len(part) - 1) if len(part) > 1 else 0
            
            transformed = part + 'F' * padding
            if rot > 0:
                transformed = transformed[-rot:] + transformed[:-rot]
            
            noise_chunk = random.choice(self.NOISE_CHUNKS)
            noise_str = f"{noise_chunk}::ERR::{i}::KEY::{transformed}::PAD::{padding}::ROT::{rot}::END::{random.randint(1000,9999)}"
            noise_list.append(noise_str)
        
        return noise_list
    
    def generate_decryptor(self, noise, fragments, iv, checksum):
        return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🔒 ERROR Protected Content</title>
<style>
html,body{{
    height:100%;
    margin:0;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
    color:white;
    font-family:'Courier New', monospace;
    overflow:auto;
}}
#loader {{
    position:fixed;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    text-align:center;
}}
.spinner {{
    width:50px;
    height:50px;
    border:3px solid #ff3333;
    border-top:3px solid #00ff00;
    border-radius:50%;
    animation:spin 1s linear infinite;
    margin:0 auto 15px;
}}
@keyframes spin {{
    0% {{ transform:rotate(0deg); }}
    100% {{ transform:rotate(360deg); }}
}}
.error-text {{
    color: #ff3333;
    font-size: 14px;
    letter-spacing: 2px;
}}
.glitch {{
    font-size: 20px;
    font-weight: bold;
    color: #ff3333;
    text-shadow: 2px 2px 0px #00ff00;
    margin-bottom: 15px;
}}
</style>
</head>
<body>
<div id="loader">
    <div class="glitch">🔒 ERROR PROTECTION 🔒</div>
    <div class="spinner"></div>
    <div class="error-text">Decrypting secure content...</div>
    <div class="error-text" style="font-size:10px; margin-top:10px;">{DEVELOPER}</div>
</div>
<script>
(function(){{
    "use strict";
    const NIBBLE = {json.dumps(self.NIBBLE_CHARS)};
    
    const nibbleMap = (() => {{
        const m = {{}};
        for(let i = 0; i < NIBBLE.length; i++) m[NIBBLE[i]] = i.toString(16);
        return m;
    }})();
    
    function decodeNibbles(s) {{
        let out = '';
        for(let i = 0; i < s.length; i++) {{
            const c = s[i];
            if(nibbleMap[c] !== undefined) out += nibbleMap[c];
            else return null;
        }}
        return out;
    }}
    
    function getKey(noise) {{
        const parts = new Array(noise.length);
        
        for(let i = 0; i < noise.length; i++) {{
            const v = noise[i];
            if(v.includes("::ERR::")) {{
                try {{
                    const segments = v.split("::");
                    let idx = -1, data = "", padding = 0, rotation = 0;
                    
                    for(let j = 0; j < segments.length; j++) {{
                        if(segments[j] === "ERR") {{
                            idx = parseInt(segments[j+1]) || 0;
                        }} else if(segments[j] === "KEY") {{
                            data = segments[j+1];
                        }} else if(segments[j] === "PAD") {{
                            padding = parseInt(segments[j+1]) || 0;
                        }} else if(segments[j] === "ROT") {{
                            rotation = parseInt(segments[j+1]) || 0;
                        }}
                    }}
                    
                    if(idx >= 0 && data) {{
                        if(rotation > 0 && data.length > rotation) {{
                            data = data.slice(rotation) + data.slice(0, rotation);
                        }}
                        if(padding > 0 && data.length > padding) {{
                            data = data.slice(0, data.length - padding);
                        }}
                        parts[idx] = data;
                    }}
                }} catch(e) {{
                    console.warn("ERROR: Failed to parse", e);
                }}
            }}
        }}
        
        let key = "";
        for(let j = 0; j < parts.length; j++) {{
            if(parts[j]) key += parts[j];
        }}
        return key;
    }}
    
    function hexToBytes(h) {{
        if(!h || h.length % 2 !== 0) return new Uint8Array(0);
        const bytes = new Uint8Array(h.length / 2);
        for(let i = 0; i < bytes.length; i++) {{
            bytes[i] = parseInt(h.substr(i * 2, 2), 16);
        }}
        return bytes;
    }}
    
    function removePadding(buffer) {{
        const padding = buffer[buffer.length - 1];
        if(padding < 1 || padding > 16) return buffer;
        for(let i = buffer.length - padding; i < buffer.length; i++) {{
            if(buffer[i] !== padding) return buffer;
        }}
        return buffer.slice(0, buffer.length - padding);
    }}
    
    async function decrypt(noise, frags, ivHex, hash) {{
        try {{
            const keyHex = getKey(noise);
            if(!keyHex || keyHex.length !== 64) {{
                throw new Error("ERROR: Key extraction failed");
            }}
            
            const cipherNibble = frags.join('');
            const cipherHex = decodeNibbles(cipherNibble);
            if(!cipherHex) {{
                throw new Error("ERROR: Ciphertext decoding failed");
            }}
            
            const keyBytes = hexToBytes(keyHex);
            const ctBytes = hexToBytes(cipherHex);
            const ivBytes = hexToBytes(ivHex);
            
            if(ctBytes.length < 16) {{
                throw new Error("ERROR: Ciphertext too short");
            }}
            
            const ciphertext = ctBytes.slice(0, ctBytes.length - 16);
            const tag = ctBytes.slice(ctBytes.length - 16);
            
            const cryptoKey = await crypto.subtle.importKey(
                'raw',
                keyBytes,
                {{name: 'AES-GCM'}},
                false,
                ['decrypt']
            );
            
            const decrypted = await crypto.subtle.decrypt(
                {{
                    name: 'AES-GCM',
                    iv: ivBytes,
                    tagLength: 128
                }},
                cryptoKey,
                new Uint8Array([...ciphertext, ...tag])
            );
            
            const unpadded = removePadding(new Uint8Array(decrypted));
            const content = new TextDecoder().decode(unpadded);
            
            const verifyHash = await crypto.subtle.digest(
                'SHA-256',
                new TextEncoder().encode(content)
            );
            const verifyHex = Array.from(new Uint8Array(verifyHash))
                .map(b => b.toString(16).padStart(2, '0'))
                .join('');
            
            if(verifyHex !== hash) {{
                throw new Error("ERROR: Integrity check failed");
            }}
            
            return content;
            
        }} catch(e) {{
            console.error("ERROR:", e);
            throw e;
        }}
    }}
    
    window.addEventListener('DOMContentLoaded', async () => {{
        const NOISE = {json.dumps(noise, ensure_ascii=False)};
        const FRAGS = {json.dumps(fragments, ensure_ascii=False)};
        const IV = "{iv}";
        const HASH = "{checksum}";
        
        try {{
            const content = await decrypt(NOISE, FRAGS, IV, HASH);
            document.open();
            document.write(content);
            document.close();
        }} catch(e) {{
            document.getElementById('loader').innerHTML = 
                '<div style="color:#ff6b6b;padding:20px;text-align:center;">' +
                '<div class="glitch">⚠️ DECRYPTION FAILED ⚠️</div>' +
                '<div class="error-text">' + e.message + '</div>' +
                '<div class="error-text" style="margin-top:10px;">Contact: {DEVELOPER}</div>' +
                '<div class="error-text">Channel: {CHANNEL}</div>' +
                '<button onclick="location.reload()" style="margin-top:20px;padding:10px 20px;background:#ff3333;border:none;color:white;border-radius:5px;cursor:pointer;">RETRY</button>' +
                '</div>';
            console.error("Decryption failed:", e);
        }}
    }});
}})();
</script>
</body>
</html>'''
    
    def encrypt_file(self, input_path, output_path=None):
        try:
            if not os.path.exists(input_path):
                print(f"❌ Error: File not found: {input_path}")
                return None
            
            self.log(f"Reading file: {input_path}")
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_size = len(content)
            self.log(f"File size: {file_size:,} bytes")
            
            if output_path is None:
                base, ext = os.path.splitext(input_path)
                output_path = f"{base}_ERROR{ext}"
            
            print(f"🔒 Encrypting: {os.path.basename(input_path)}")
            
            start_time = datetime.now()
            
            self.log("Step 1: Encrypting content...")
            encrypted = self.encrypt_content_fast(content)
            
            self.log("Step 2: Converting to nibble format...")
            ciphertext_bytes = bytes.fromhex(encrypted['encrypted'])
            nibbles = self.bytes_to_hex_nibbles(ciphertext_bytes)
            
            self.log("Step 3: Creating fragments...")
            fragments = self.split_fragments_fast(nibbles, 6)
            
            self.log("Step 4: Hiding encryption key...")
            noise = self.hide_key_in_noise_fast(encrypted['key'], 6)
            
            self.log("Step 5: Generating protected file...")
            final_html = self.generate_decryptor(noise, fragments, encrypted['iv'], encrypted['checksum'])
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            output_size = len(final_html)
            
            print(f"✅ Success! Encrypted file created: {output_path}")
            print(f"   Original size: {file_size:,} bytes")
            print(f"   Protected size: {output_size:,} bytes")
            print(f"   Encryption time: {duration:.2f} seconds")
            print(f"   🔑 Key fragments: {len(noise)}")
            print(f"   🔒 Ciphertext fragments: {len(fragments)}")
            print(f"   🔐 Developer: {DEVELOPER}")
            print(f"   📢 Channel: {CHANNEL}")
            
            return output_path
            
        except Exception as e:
            print(f"❌ Encryption failed: {str(e)}")
            return None
    
    def batch_encrypt(self, file_patterns, output_dir="protected"):
        import glob
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        results = []
        for pattern in file_patterns:
            files = glob.glob(pattern)
            for file in files:
                if os.path.isfile(file):
                    print(f"\n{'='*50}")
                    print(f"Processing: {file}")
                    output_name = os.path.join(output_dir, f"ERROR_{os.path.basename(file)}")
                    result = self.encrypt_file(file, output_name)
                    if result:
                        results.append(result)
        
        print(f"\n{'='*50}")
        print(f"✅ Batch complete! {len(results)} files encrypted")
        return results

def main():
    parser = argparse.ArgumentParser(
        description="ERROR HTML Encryption Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s index.html                    # Encrypt single file
  %(prog)s index.html -o protected.html  # Specify output file
  %(prog)s *.html -b                     # Batch encrypt all HTML files
  %(prog)s page.html -v                  # Verbose mode

Developer: {DEVELOPER}
Channel: {CHANNEL}
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input file to encrypt')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-b', '--batch', action='store_true', help='Batch encrypt files')
    parser.add_argument('-d', '--dir', default='protected', help='Output directory for batch mode')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if not args.input:
        print("ERROR HTML Encryption Tool")
        print("=" * 50)
        print(f"Developer: {DEVELOPER}")
        print(f"Channel: {CHANNEL}")
        print("=" * 50)
        
        input_file = input("Enter file path to encrypt: ").strip().strip('"\'')
        
        if not input_file:
            print("No file specified.")
            return
        
        output_file = input("Output file (press Enter for auto-name): ").strip().strip('"\'')
        if not output_file:
            output_file = None
        
        encryptor = ERRORHTMLEncryptor(verbose=args.verbose)
        encryptor.encrypt_file(input_file, output_file)
        
    else:
        encryptor = ERRORHTMLEncryptor(verbose=args.verbose)
        
        if args.batch:
            import glob
            files = glob.glob(args.input)
            if not files:
                print(f"No files found matching pattern: {args.input}")
                return
            
            print(f"Found {len(files)} file(s) to encrypt:")
            for f in files:
                print(f"  - {f}")
            
            confirm = input("\nProceed with encryption? (y/N): ").lower()
            if confirm == 'y':
                encryptor.batch_encrypt([args.input], args.dir)
        else:
            encryptor.encrypt_file(args.input, args.output)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Cancelled by user")
        sys.exit(0)