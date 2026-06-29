
@RestController
@RequestMapping("/api/suppliers")
public class SupplierController {

    @Autowired
    private SupplierService supplierService;

    @GetMapping("/")
    public ApiResponse<List<Supplier>> listSuppliers() {
        List<Supplier> suppliers = supplierService.getAllSuppliers();
        return ApiResponse.success(suppliers);
    }

    @GetMapping("/{id}")
    public ApiResponse<Supplier> getSupplier(@PathVariable Long id) {
        Supplier supplier = supplierService.getSupplierById(id);
        if (supplier == null) {
            return ApiResponse.error(404, "供应商不存在");
        }
        return ApiResponse.success(supplier);
    }

    @PostMapping("/")
    public ApiResponse<Supplier> createSupplier(@RequestBody Supplier supplier) {
        Supplier created = supplierService.createSupplier(supplier);
        return ApiResponse.success("供应商创建成功", created);
    }

    @PutMapping("/{id}")
    public ApiResponse<Supplier> updateSupplier(@PathVariable Long id,
                                                 @RequestBody Supplier supplier) {
        try {
            Supplier updated = supplierService.updateSupplier(id, supplier);
            return ApiResponse.success("供应商更新成功", updated);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(404, e.getMessage());
        }
    }

    @DeleteMapping("/{id}")
    public ApiResponse<Void> deleteSupplier(@PathVariable Long id) {
        try {
            supplierService.deleteSupplier(id);
            return ApiResponse.success("供应商删除成功", null);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(404, e.getMessage());
        }
    }
}