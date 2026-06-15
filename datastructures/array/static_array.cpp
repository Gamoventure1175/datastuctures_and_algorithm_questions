/*
Trying to learn static array and its internal implementation
*/

// This would be useful if this file was a header '.h' file
// #pragma once

#include <cstddef>
#include <stdexcept>
#include <algorithm>
#include <iterator>
#include <iostream>

template <typename T, std::size_t N>
class StaticArray {
public:
    using value_type             = T;
    using size_type              = std::size_t;
    using difference_type        = std::ptrdiff_t;

    using reference              = T&;
    using const_reference        = const T&;

    using pointer                = T*;
    using const_pointer          = const T*;

    using iterator               = T*;
    using const_iterator         = const T*;

    using reverse_iterator       = std::reverse_iterator<iterator>;
    using const_reverse_iterator = std::reverse_iterator<const_iterator>;

private:
    T data_[N];

public:

    // -------------------------
    // Constructors
    // -------------------------

    // The empty {} inside the initializer list forces zero-initialization
    // constexpr StaticArray() : data_{} {}

    // -------------------------
    // Element Access
    // -------------------------

    constexpr reference operator[](size_type index) noexcept {
        return data_[index];
    }

    constexpr const_reference operator[](size_type index) const noexcept {
        return data_[index];
    }

    reference at(size_type index) {
        if (index >= N) {
            throw std::out_of_range("StaticArray::at - index out of range");
        }

        return data_[index];
    }

    const_reference at(size_type index) const {
        if (index >= N) {
            throw std::out_of_range("StaticArray::at - index out of range");
        }

        return data_[index];
    }

    constexpr reference front() noexcept {
        return data_[0];
    }

    constexpr const_reference front() const noexcept {
        return data_[0];
    }

    constexpr reference back() noexcept {
        return data_[N - 1];
    }

    constexpr const_reference back() const noexcept {
        return data_[N - 1];
    }

    constexpr pointer data() noexcept {
        return data_;
    }

    constexpr const_pointer data() const noexcept {
        return data_;
    }

    // -------------------------
    // Capacity
    // -------------------------

    [[nodiscard]]
    constexpr bool empty() const noexcept {
        return N == 0;
    }

    [[nodiscard]]
    constexpr size_type size() const noexcept {
        return N;
    }

    [[nodiscard]]
    constexpr size_type max_size() const noexcept {
        return N;
    }

    // -------------------------
    // Iterators
    // -------------------------

    constexpr iterator begin() noexcept {
        return data_;
    }

    constexpr const_iterator begin() const noexcept {
        return data_;
    }

    constexpr const_iterator cbegin() const noexcept {
        return data_;
    }

    constexpr iterator end() noexcept {
        return data_ + N;
    }

    constexpr const_iterator end() const noexcept {
        return data_ + N;
    }

    constexpr const_iterator cend() const noexcept {
        return data_ + N;
    }

    constexpr reverse_iterator rbegin() noexcept {
        return reverse_iterator(end());
    }

    constexpr const_reverse_iterator rbegin() const noexcept {
        return const_reverse_iterator(end());
    }

    constexpr reverse_iterator rend() noexcept {
        return reverse_iterator(begin());
    }

    constexpr const_reverse_iterator rend() const noexcept {
        return const_reverse_iterator(begin());
    }

    // -------------------------
    // Modifiers
    // -------------------------

    void fill(const T& value) {
        std::fill(begin(), end(), value);
    }

    void swap(StaticArray& other)
        noexcept(std::is_nothrow_swappable_v<T>)
    {
        std::swap_ranges(begin(), end(), other.begin());
    }

    // -------------------------
    // Comparisons
    // -------------------------

    bool operator==(const StaticArray& other) const {
        return std::equal(begin(), end(), other.begin(), other.end());
    }

    bool operator!=(const StaticArray& other) const {
        return !(*this == other);
    }

    bool operator<(const StaticArray& other) const {
        return std::lexicographical_compare(
            begin(), end(),
            other.begin(), other.end()
        );
    }

    bool operator>(const StaticArray& other) const {
        return other < *this;
    }

    bool operator<=(const StaticArray& other) const {
        return !(other < *this);
    }

    bool operator>=(const StaticArray& other) const {
        return !(*this < other);
    }
};

template <typename T, size_t N>
void printStaticArray(const StaticArray<T, N>& s) {
    for (auto &ele : s) {
        std::cout << ele << std::endl;
    }
}

int main() {

    StaticArray<int, 5> sample;

    printStaticArray(sample);


    return 0;
}