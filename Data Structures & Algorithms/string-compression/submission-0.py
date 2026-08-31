class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0,0

        while read < len(chars):

            # remember character we are currently compressing
            char_to_compress = chars[read]
            start = read

            while read < len(chars) and chars[read] == char_to_compress:
                read +=1

            # Calculate length of group, read - start
            count = read - start

            # Write the characeter to write pointer
            chars[write] = char_to_compress
            write +=1

            # If count > 1, write each digit count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write +=1
        return write
        


        