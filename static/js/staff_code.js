document.addEventListener("DOMContentLoaded", function () {
  const roleField = document.getElementById("id_role");
  const codeField = document.getElementById("id_staff_code");

  function generateCode(prefix) {
    const randomNum = Math.floor(1000 + Math.random() * 9000);
    return `${prefix}${randomNum}`;
  }

  if (roleField && codeField) {
    roleField.addEventListener("change", function () {
      if (!codeField.value || codeField.value.trim() === "") {
        if (roleField.value === "Intern") {
          codeField.value = generateCode("nxrint");
        } else if (roleField.value === "Employee") {
          codeField.value = generateCode("nxremp");
        } else {
          codeField.value = "";
        }
      }
    });

    // Trigger code generation on page load
    if (roleField.value === "Intern") {
      codeField.value = generateCode("nxrint");
    } else if (roleField.value === "Employee") {
      codeField.value = generateCode("nxremp");
    }
  }
});
