// rust_inference/src/lib.rs
use std::slice;

#[no_mangle]
pub extern "C" fn generate_notes(input_ptr: *const f32, len: usize) -> f32 {
    let input = unsafe { slice::from_raw_parts(input_ptr, len) };
    println!("Rust received input: {:?}", input);
    0.42 // Dummy output
}
