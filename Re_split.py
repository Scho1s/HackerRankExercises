regex_pattern = r"[,.]{1}"

import re
print("\n".join(re.split(regex_pattern, input())))