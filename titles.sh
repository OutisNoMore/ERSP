# All target phones
PHONES=("blubold"
        "galaxy"
        "pixel2"
        "pixel3a"
        "pixel3a2"
        "pixel6a"
        "audiomoth"
        "audiomoth2"
        "audiomoth3"
        "audiomoth4")

for phone in "${PHONES[@]}"; do
  # Check if file of confidences exists for phone
  if [ -f *$phone-* ]; then
    # Rename results to phone name
    mv *$phone-* $phone
  fi
done

